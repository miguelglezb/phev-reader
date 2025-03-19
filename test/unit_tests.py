import pytest
import numpy as np
from pathlib import Path
import phev.phev 
import phev.units


@pytest.fixture
def select_evfile(request):
    """Fixture that returns a full path to the requested EV file."""
    return Path("./data") / request.param

@pytest.fixture
def get_all_evfiles():
    return list(Path("./data").glob("*.ev"))


class TestPhev:
    
    def test_evdf(self, get_all_evfiles):
        for evfile in get_all_evfiles:
            evdf = phev.phev.evreader(evfile)
            assert evdf is not None
            assert isinstance(evdf, phev.phev.Evdf)

    @pytest.mark.parametrize(
        "select_evfile,col_name,quants",
        [
            ("./data/separation_vs_time.ev", "time", "time"),
            ("./data/energy.ev", "total energy", "energy"),
        ],
    )
    def test_phys_quantities(self, select_evfile, col_name, quants):
        """Test using the select_evfile fixture."""
        evdf = phev.phev.evreader(select_evfile)
        assert evdf.column_physical_quantity(col_name) == quants

    @pytest.mark.parametrize("select_evfile", ["mock_separation.ev"], indirect=True)
    def test_unknown_phys_quantities(self, select_evfile):
        """Test using the select_evfile fixture."""
        evdf = phev.phev.evreader(select_evfile)
        assert evdf.column_physical_quantity("unicorn_mass") == "Unknown quantity"

    @pytest.mark.parametrize("select_evfile", ["mtSink0001N01.ev"], indirect=True)
    def test_ph_units(self, select_evfile):
        evdf = phev.phev.evreader(select_evfile)
        assert evdf.column_units("time") == "ph. time units"
        assert evdf.column_units("x") == "ph. distance units"
        assert evdf.column_units("y") == "ph. distance units"
        assert evdf.column_units("z") == "ph. distance units"
        assert evdf.column_units("mass") == "ph. mass units"
        assert evdf.column_units("vx") == "ph. velocity units"
        assert evdf.column_units("vy") == "ph. velocity units"
        assert evdf.column_units("vz") == "ph. velocity units"
        assert not evdf.column_units("mass") == "mesa mass units"

    @pytest.mark.parametrize("select_evfile", ["mock_separation.ev"], indirect=True)
    def test_ph_unknown_units(self, select_evfile):
        evdf = phev.phev.evreader(select_evfile)
        assert evdf.column_units("unicorn_mass") == "Unknown units"

    def test_conversion_rate_default(self, get_all_evfiles):
        for evfile in get_all_evfiles:
            evdf = phev.phev.evreader(evfile)        
            for col_name in evdf.keys():
                assert evdf.column_conversion_rate(col_name) == 1.0

    @pytest.mark.parametrize("select_evfile", ["mtSink0001N01.ev"], indirect=True)
    def test_conversion(self, select_evfile):
        evdf = phev.phev.evreader(select_evfile)
        orig_column_time = evdf["time"]
        orig_column_x = evdf["x"]
        orig_column_mass = evdf["mass"]
        orig_column_vx = evdf["vx"]
        evdf.convert_units(column_key="time", new_units="yr")
        evdf.convert_units(column_key="x", new_units="cm")
        evdf.convert_units(column_key="mass", new_units="tons")
        evdf.convert_units(column_key="vx", new_units="km/s")

        assert np.array_equal(
            orig_column_time.values * phev.units.years, evdf["time"].values
        )
        assert np.array_equal(
            orig_column_x.values * phev.units.centimeters, evdf["x"].values
        )
        assert np.array_equal(orig_column_vx.values * phev.units.km_s, evdf["vx"].values)
        assert np.array_equal(orig_column_mass.values * phev.units.tons, evdf["mass"].values)

    @pytest.mark.parametrize("select_evfile", ["mtSink0001N01.ev"], indirect=True)
    def test_unknown_conversion(self, select_evfile):
        evdf = phev.phev.evreader(select_evfile, pheaders=False)
        evdf_converted_to_dropbears = evdf.copy()
        dropbear_conversion_rate = 666.42069
        evdf_converted_to_dropbears.convert_units(
            column_key="x",
            new_units="dropbears",
            new_conversion_val=dropbear_conversion_rate,
            warning_new_conv_val=False,
        )

        assert np.array_equal(
            evdf["x"].values * dropbear_conversion_rate,
            evdf_converted_to_dropbears["x"].values,
        )
        evdf_converted_to_dropbears.convert_units(
            column_key="x",
            new_units="ph.time units",
            new_conversion_val=1,
            warning_new_conv_val=False,
        )
        assert np.array_equal(evdf_converted_to_dropbears["x"].values, evdf["x"].values)
