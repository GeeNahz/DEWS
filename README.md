# DEWS
A Drought Early Warning System for northern Nigeria

The endpoint is: https://dewsapp.herokuapp.com/dews/pred/


Supported request Methods: GET --> returns only an HttpResponse with the text "Home page?". Don't laugh please...
                           
POST --> returns the Year, Drought index (which is the true prediction), Ocean temperature(SST) and Climate direction(ITCZ).

receives an object with year, state and lga (local government area) as the keys of the form {year: <year_value>, state: <state_value>, lga: <lga_value>}.

For accessing the return object, you should use:

'year' for Year,

'drought_index' for Drought index,

'ocean_temperature' for Ocean temperature,

'climate_direction' for Climate direction.

'SPEI_april' for Drought index for the month of April. (Do the same for May through October)

'region' for the region of the selected LGA.
