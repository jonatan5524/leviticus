import * as React from 'react';
import MyAppBar from './components/MyAppBar';
import Root from './routes/root';
import Category from './routes/Category';
import { categories } from './api/categories';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import logo from './assets/policeLogo.png';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root categories={categories} />,
  },
  {
    path: '/category',
    element: <Category />,
  },
]);

function App() {
  return (
    <>
      <MyAppBar />
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: '100vh',
         }}
      >
        <img src={logo} alt="Logo" style={{
          height: '30vh',
          width: '20vw',
          opacity: '0.5'
        }} />
        
        <RouterProvider router={router} />
        <img src={logo} alt="Logo" style={{
          height: '30vh',
          width: '20vw',
          opacity: '0.5'
        }} />
      </div>
    </>
  );
}

export default App;
