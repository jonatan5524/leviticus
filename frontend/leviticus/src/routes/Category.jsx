import * as React from 'react';
import { Typography, Button, Grid } from '@mui/material';
import { createStyles, makeStyles } from '@material-ui/core/styles';
import SiteList from '../components/SiteList';
import { useLocation } from 'react-router-dom';

const useStyles = makeStyles(() =>
  createStyles({
    title: {
      flexGrow: 1,
      textAlign: 'center',
    },
  })
);

export default function Root() {
  const location = useLocation();
  const { from } = location.state;

  const list = [
    'test1.com',
    'test2.com',
    'test3.com',
    'test4.com',
    'test5.com',
    'test6.com',
  ];

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
            {from}
          </Typography>
          <SiteList />
        </Grid>
      </Grid>
    </>
  );
}
