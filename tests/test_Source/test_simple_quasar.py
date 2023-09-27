from sim_pipeline.Sources.quasar_catalog import simple_quasar
import pytest


def test_simple_quasar():
    catalog = simple_quasar.quasar_catalog(n = 1000, z_min = 0.1, z_max = 5, 
                                           m_min = 17, m_max = 23)
    column_names = ["z", "mag_r", "mag_g", "mag_i"]
    assert catalog.colnames[0] == column_names[0]
    assert catalog.colnames[1] == column_names[1]
    assert catalog.colnames[2] == column_names[2]
    assert catalog.colnames[3] == column_names[3]

if __name__ == "__main__":
    pytest.main()
