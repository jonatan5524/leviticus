import React from 'react';
import { createStyles, makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
// import MenuIcon from '@material-ui/icons/Menu';
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
          {/* <IconButton
            edge='start'
            className={classes.menuButton}
            color='inherit'
            aria-label='menu'
          >
            <MenuIcon />
          </IconButton> */}
          <img src={logo} alt='Leviticus' className={classes.logo} />
          <Typography variant='h6' className={classes.title}>
            Leviticus
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}
