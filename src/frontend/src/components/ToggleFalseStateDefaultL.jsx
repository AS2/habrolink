import { useMemo } from "react";
import styles from "./ToggleFalseStateDefaultL.module.css";

const ToggleFalseStateDefaultL = ({
  group1,
  radioButton,
  toggleFalseStateDefaultLPosition,
  toggleFalseStateDefaultLTop,
  toggleFalseStateDefaultLLeft,
  radioButtonFontFamily,
}) => {
  const toggleFalseStateDefaultLStyle = useMemo(() => {
    return {
      position: toggleFalseStateDefaultLPosition,
      top: toggleFalseStateDefaultLTop,
      left: toggleFalseStateDefaultLLeft,
    };
  }, [
    toggleFalseStateDefaultLPosition,
    toggleFalseStateDefaultLTop,
    toggleFalseStateDefaultLLeft,
  ]);

  const radioButtonStyle = useMemo(() => {
    return {
      fontFamily: radioButtonFontFamily,
    };
  }, [radioButtonFontFamily]);

  return (
    <div
      className={styles.togglefalseStatedefaultL}
      style={toggleFalseStateDefaultLStyle}
    >
      <img
        className={styles.togglefalseStatedefaultLChild}
        alt=""
        src={group1}
      />
      <div className={styles.radioButton} style={radioButtonStyle}>
        {radioButton}
      </div>
    </div>
  );
};

export default ToggleFalseStateDefaultL;
