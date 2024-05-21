import styles from "./HabrolinkerEnumField.module.css";
import { useCallback, useState, useEffect } from "react";

const HabrolinkerEnumField = ({ label, enumeration, value, onChangeValue }) => {
  const [currentIndex, setCurrentIndex] = useState(value == null ? 0 : value);

  const onValueChanged = useCallback(event => {
    let curValue = event.target.value;
    setCurrentIndex(curValue)
    if (onChangeValue != null)
      onChangeValue(curValue);
  }, [currentIndex]);

  useEffect(() => {
    setCurrentIndex(value == null ? 0 : value);
  }, [value]);

  return (
    <div className={styles.textField}>
      <div className={styles.partInputLabel}>
        <b className={styles.label}>{label}</b>
      </div>
      <select className={styles.inputField} onInput={onValueChanged} value={currentIndex}>
        {enumeration.map((elem, i) => (
          <option key={i} value={i}>{elem}</option>
        ))}
      </select>
    </div>
  );
};

export default HabrolinkerEnumField;
