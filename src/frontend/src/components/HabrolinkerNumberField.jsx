import TypeTextCombinedFalseFil from "./TypeTextCombinedFalseFil";
import styles from "./HabrolinkerNumberField.module.css";
import { useCallback, useState, useEffect } from "react";

const HabrolinkerNumberField = ({ label, placeholder, value, onChangeValue }) => {
  const [currentNumber, setCurrentNumber] = useState(value == null ? 0 : value);

  const onValueChanged = useCallback(event => {
    let curValue = event.target.value;
    setCurrentNumber(curValue)
    if (onChangeValue != null)
      onChangeValue(curValue);
  }, [currentNumber]);

  useEffect(() => {
    setCurrentNumber(value == null ? 0 : value);
  }, [value]);

  return (
    <div className={styles.textField}>
      <div className={styles.partInputLabel}>
        <b className={styles.label}>{label}</b>
      </div>
      <input type="number" className={styles.inputField} onInput={onValueChanged} value={currentNumber} />
    </div>
  );
};

export default HabrolinkerNumberField;
