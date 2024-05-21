import styles from "./HabrolinkerEnumField.module.css";
import { useCallback, useState, useEffect } from "react";

const HabrolinkerDateField = ({ label, onChangeValue, value }) => {
  const [currentDate, setCurrentDate] = useState(value == null ? "" : value);

  const onValueChanged = useCallback(event => {
    let curValue = event.target.value;
    setCurrentDate(curValue)
    if (onChangeValue != null)
      onChangeValue(curValue);
  }, [currentDate]);

  useEffect(() => {
    setCurrentDate(value == null ? "" : value);
  }, [value]);

  return (
    <div className={styles.textField}>
      <div className={styles.partInputLabel}>
        <b className={styles.label}>{label}</b>
      </div>
      <input type="date" className={styles.inputField} onInput={onValueChanged} value={currentDate} />
    </div>
  );
};

export default HabrolinkerDateField;
