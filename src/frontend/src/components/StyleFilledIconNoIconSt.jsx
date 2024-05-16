import { useMemo } from "react";
import styles from "./StyleFilledIconNoIconSt.module.css";

const StyleFilledIconNoIconSt = ({
  button,
  styleFilledIconNoIconStBackgroundColor,
  buttonFontWeight,
  onButtonStyle1Click,
}) => {
  const styleFilledIconNoIconStStyle = useMemo(() => {
    return {
      backgroundColor: styleFilledIconNoIconStBackgroundColor,
    };
  }, [styleFilledIconNoIconStBackgroundColor]);

  const buttonStyle = useMemo(() => {
    return {
      fontWeight: buttonFontWeight,
    };
  }, [buttonFontWeight]);

  return (
    <div
      className={styles.stylefilledIconnoIconSt}
      style={styleFilledIconNoIconStStyle}
      onClick={onButtonStyle1Click}
    >
      <div className={styles.button} style={buttonStyle}>
        {button}
      </div>
    </div>
  );
};

export default StyleFilledIconNoIconSt;
