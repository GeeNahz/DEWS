import { useState } from 'react';

function App() {

  const [info, setInfo] = useState('');

  function fetchData(payload) {
    // let url = 'http://127.0.0.1:8000/dews/pred/';
    let url = 'https://dewsapp.herokuapp.com/dews/pred/';

    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload)
    }).then(res => {
      return res.json()
    }).then(data => {
      return setInfo(data)
    }).catch(err => console.error('Error found:',err))
  }

  const payload = {
    'state': 'KEBBI',
    'year': 2025
  }


  return (
    <div className="App">
      <h2>Drought App Here!!!</h2>

      <button onClick={() => { fetchData(payload) }} >Submit</button>
      {info ? <div>
            <h2>{ info.drought_index }</h2>
            <p>{ info.ocean_temperature }</p>
            <p>{ info.climate_direction }</p>
            <p>For the year: { info.year }</p>
          </div>
         : <p>No data yet...</p> }
    </div>
  );
}

export default App;
