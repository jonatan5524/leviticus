import * as React from 'react';
import MyAppBar from './components/MyAppBar';
import Root from './routes/root';
import Category from './routes/Category';
import { categories } from './api/categories';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

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
        <RouterProvider router={router} />
      </div>
    </>
  );
}

export default App;
