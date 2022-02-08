# DEWS
A Drought Early Warning System for northern Nigeria

The endpoint is: https://dewsapp.herokuapp.com/dews/pred/

Supported request Methods: GET --> returns only an HttpResponse with the text "Home page?". Don't laugh please...
                           \t\t\nPOST --> returns the Year, Drought index (which is the true prediction), Ocean temperature(SST) and Climate direction(ITCZ).
                                    \t\t\t\nreceives an object with year and month as the keys of the form {year: <year_value>, month: <month_value>}.
                                    \t\t\t\nFor accessing the return object, you should use:
                                        \t\t\t\t\n'year' for Year,
                                        \t\t\t\t\n'drought_index' for Drought index,
                                        \t\t\t\t\n'ocean_temperature' for Ocean temperature,
                                        \t\t\t\t\n'climate_direction' for Climate direction.
