import * as React from 'react';
import { Typography, Button, Grid } from '@mui/material';
import { createStyles, makeStyles } from '@material-ui/core/styles';
import { Outlet, Link } from 'react-router-dom';
import axios from 'axios';

const useStyles = makeStyles(() =>
  createStyles({
    title: {
      flexGrow: 1,
      textAlign: 'center',
    },
  })
);

export default function Root() {
  const [categories, setCategories] = React.useState([]);

  React.useEffect(() => {
    axios
      .get(
        `https://g4d3d36de9bbc09-db1.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/categorysites/`
      )
      .then(({ data: { items } }) => {
        const newCategories = [...new Set(items.map((item) => item.category))];

        setCategories(newCategories);
      });
  }, []);

  return (
    <>
      <Grid
        container
        direction='column'
        justifyContent='center'
        alignItems='center'
        spacing={3}
      >
        <Grid item>
          <Typography variant='h4' align='center'>
            Pick a category
          </Typography>
        </Grid>
        {categories.map((category, index) => (
          <Grid item key={index}>
            <Link to='/category' state={{ from: category }}>
              <Button
                style={{ width: 150, height: 50, borderRadius: 15}}
                size='large'
                variant='contained'
                color='primary'
                fullWidth
              >
                {category}
              </Button>
            </Link>
          </Grid>
        ))}
      </Grid>
    </>
  );
}
