import { useMemo } from "react";
import FilledNoStateDefaultSize from "./FilledNoStateDefaultSize";
import styles from "./HabrRating.module.css";

const HabrRating = ({
  prop,
  label,
  label1,
  propOverflow,
  propWidth,
  showIcon,
}) => {
  const filledNoStateDefaultSizeStyle = useMemo(() => {
    return {
      overflow: propOverflow,
      width: propWidth,
    };
  }, [propOverflow, propWidth]);

  return (
    <div className={styles.habrRating}>
      <b className={styles.b}>{prop}</b>
      <div className={styles.yerasField}>
        <FilledNoStateDefaultSize
          tangoUser="/tangolock.svg"
          label="4.5"
          showIcon={false}
          filledNoStateDefaultSizeWidth="78px"
          filledNoStateDefaultSizeHeight="27px"
          filledNoStateDefaultSizePadding="0px var(--padding-base)"
          filledNoStateDefaultSizeOverflow="unset"
          filledNoStateDefaultSizeAlignSelf="unset"
          labelFontFamily="'Inria Sans'"
        />
        <div className={styles.div}>-</div>
        <FilledNoStateDefaultSize
          tangoUser="/tangolock1.svg"
          label="5"
          showIcon={false}
          filledNoStateDefaultSizeWidth="unset"
          filledNoStateDefaultSizeHeight="27px"
          filledNoStateDefaultSizePadding="0px var(--padding-base)"
          filledNoStateDefaultSizeOverflow="hidden"
          filledNoStateDefaultSizeAlignSelf="unset"
          labelFontFamily="'Inria Sans'"
        />
      </div>
    </div>
  );
};

export default HabrRating;
