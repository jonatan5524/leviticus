import * as React from 'react';
import { Typography, Button, Grid } from '@mui/material';
import { createStyles, makeStyles } from '@material-ui/core/styles';
import SiteList from '../components/SiteList';
import { useLocation } from 'react-router-dom';
import { Link } from 'react-router-dom';
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
  const location = useLocation();
  const { from } = location.state;

  const [sites, setSites] = React.useState([]);

  React.useEffect(() => {
    axios
      .get(
        `https://g4d3d36de9bbc09-db1.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/categorysites/`
      )
      .then(({ data: { items } }) => {
        const newSites = items
          .filter(({ category }) => category === from)
          .map(({ site }) => site);

        setSites(newSites);
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
        <Link to='/'>
        <Button
                style={{ width: 150, height: 50, borderRadius: 15 }}
                size='large'
                variant='contained'
                color='primary'
                fullWidth
              >
                Home
              </Button>
        </Link>
        <Grid item>
          <Typography variant='h4' align='center'>
            {from}
          </Typography>
          <SiteList list={sites} />
        </Grid>
      </Grid>
    </>
  );
}
