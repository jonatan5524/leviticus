import * as React from 'react';
import MyAppBar from './components/MyAppBar';
import Root from './routes/root';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
  },
]);

function App() {
  return (
    <>
      <div>
        <MyAppBar />
        <RouterProvider router={router} />
      </div>
    </>
  );
}

export default App;
