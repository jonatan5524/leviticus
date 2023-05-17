import React from 'react';
import { createStyles, makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import logo from '../assets/policeLogo.png';

const useStyles = makeStyles(() =>
  createStyles({
    root: {
      flexGrow: 1,
    },
    title: {
      flexGrow: 1,
      textAlign: 'center',
    },
    logo: {
      maxWidth: 40,
      marginRight: '10px',
         },
  })
);

export default function MyAppBar() {
  const classes = useStyles();

  return (
    <div>
      <AppBar>
        <Toolbar>
          <img src={logo} alt='Leviticus' className={classes.logo} />
          <Typography variant='h4' className={classes.title}>
            Leviticus
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}
