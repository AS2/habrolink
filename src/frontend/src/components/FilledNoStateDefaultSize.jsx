import { useMemo } from "react";
import styles from "./FilledNoStateDefaultSize.module.css";

const FilledNoStateDefaultSize = ({
  tangoUser,
  label = "Name",
  showIcon = true,
  filledNoStateDefaultSizeWidth,
  filledNoStateDefaultSizeHeight,
  filledNoStateDefaultSizePadding,
  filledNoStateDefaultSizeOverflow,
  filledNoStateDefaultSizeAlignSelf,
  labelFontFamily,
}) => {
  const filledNoStateDefaultSizeStyle = useMemo(() => {
    return {
      width: filledNoStateDefaultSizeWidth,
      height: filledNoStateDefaultSizeHeight,
      padding: filledNoStateDefaultSizePadding,
      overflow: filledNoStateDefaultSizeOverflow,
      alignSelf: filledNoStateDefaultSizeAlignSelf,
    };
  }, [
    filledNoStateDefaultSizeWidth,
    filledNoStateDefaultSizeHeight,
    filledNoStateDefaultSizePadding,
    filledNoStateDefaultSizeOverflow,
    filledNoStateDefaultSizeAlignSelf,
  ]);

  const labelStyle = useMemo(() => {
    return {
      fontFamily: labelFontFamily,
    };
  }, [labelFontFamily]);

  return (
    <div
      className={styles.fillednoStatedefaultSize}
      style={filledNoStateDefaultSizeStyle}
    >
      {showIcon && (
        <img className={styles.tangouserIcon} alt="" src={tangoUser} />
      )}
      <div className={styles.label} style={labelStyle}>
        {label}
      </div>
    </div>
  );
};

export default FilledNoStateDefaultSize;
