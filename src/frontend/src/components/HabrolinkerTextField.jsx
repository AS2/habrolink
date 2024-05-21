import TypeTextCombinedFalseFil from "./TypeTextCombinedFalseFil";
import styles from "./HabrolinkerTextField.module.css";
import { useCallback, useState, useEffect } from "react";

const HabrolinkerTextField = ({ label, placeholder, value, onChangeValue }) => {
  const [helperText, setHelperText] = useState(value == null ? "0/100" : String(value.length) + "/100");
  const [currentText, setCurrentText] = useState(value == null ? "" : value);

  const onValueChanged = useCallback(event => {
    let curValue = event.target.value;
    if (curValue.length > 100) {
      curValue = curValue.substring(0, 100)
    }
    setCurrentText(curValue);
    setHelperText(String(curValue.length) + "/100");
    if (onChangeValue != null)
      onChangeValue(curValue);
  }, [helperText, currentText]);

  useEffect(() => {
    setCurrentText(value == null ? "" : value);
    setHelperText(value == null ? "0/100" : String(value.length) + "/100");
  }, [value]);

  return (
    <div className={styles.textField}>
      <div className={styles.partInputLabel}>
        <b className={styles.label}>{label}</b>
      </div>
      <input className={styles.inputField} onInput={onValueChanged} value={currentText} placeholder={placeholder} />
      <div className={styles.partInputHelper}>
        <div className={styles.helperText}>{helperText}</div>
      </div>
    </div>
  );
};

export default HabrolinkerTextField;
