import { useMemo } from "react";
import styles from "./StateFilled.module.css";

const StateFilled = ({
  labelText = "Label",
  prefix = "$",
  inputText = "Input Text",
  eye,
  helperText = "Helper Text",
  showHelperText = false,
  showPrefix = false,
  showIcon = false,
  stateFilledWidth,
  stateFilledBorderRadius,
  stateFilledFlex,
  frameDivBackgroundColor,
  frameDivWidth,
  helperTextWidth,
  helperTextAlignSelf,
}) => {
  const stateFilledStyle = useMemo(() => {
    return {
      width: stateFilledWidth,
      borderRadius: stateFilledBorderRadius,
      flex: stateFilledFlex,
    };
  }, [stateFilledWidth, stateFilledBorderRadius, stateFilledFlex]);

  const frameDivStyle = useMemo(() => {
    return {
      backgroundColor: frameDivBackgroundColor,
      width: frameDivWidth,
    };
  }, [frameDivBackgroundColor, frameDivWidth]);

  const helperTextStyle = useMemo(() => {
    return {
      width: helperTextWidth,
      alignSelf: helperTextAlignSelf,
    };
  }, [helperTextWidth, helperTextAlignSelf]);

  return (
    <div className={styles.statefilled} style={stateFilledStyle}>
      <div className={styles.field}>
        <div className={styles.frameParent} style={frameDivStyle}>
          <div className={styles.frame}>
            <div className={styles.lable}>{labelText}</div>
            <div className={styles.frameInner}>
              <div className={styles.textWrapper}>
                <div className={styles.text}>
                  {showPrefix && <div className={styles.prefix}>{prefix}</div>}
                  <div className={styles.inputText}>{inputText}</div>
                </div>
              </div>
            </div>
          </div>
          {showIcon && <img className={styles.eyeIcon} alt="" src={eye} />}
        </div>
      </div>
      {showHelperText && (
        <div className={styles.helperText} style={helperTextStyle}>
          <div className={styles.helperText1}>{helperText}</div>
        </div>
      )}
    </div>
  );
};

export default StateFilled;
