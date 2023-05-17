import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <div style={{ background: '#D2E9E9',
   backgroundPosition: 'center',
   backgroundSize: 'cover',
   backgroundRepeat: 'no-repeat',
   width: '99vw',
   height: '98vh'}}>
    <App/>
    </div>
  </React.StrictMode>
);
