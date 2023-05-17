import * as React from 'react';
import { Typography, Button, Grid } from '@mui/material';
import { createStyles, makeStyles } from '@material-ui/core/styles';
import { Outlet, Link } from 'react-router-dom';

const useStyles = makeStyles(() =>
  createStyles({
    title: {
      flexGrow: 1,
      textAlign: 'center',
    },
  })
);

export default function Root({ categories }) {
  const classes = useStyles();

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
