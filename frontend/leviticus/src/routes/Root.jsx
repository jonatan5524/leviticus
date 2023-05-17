import * as React from 'react';
import Typography from '@material-ui/core/Typography';
import { createStyles, makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(() =>
  createStyles({
    title: {
      flexGrow: 1,
      textAlign: 'center',
    },
  })
);

export default function Root() {
  const classes = useStyles();

  return (
    <>
      <div>
        <Typography variant='h2' className={classes.title}>
          Pick a category
        </Typography>
      </div>
    </>
  );
}
