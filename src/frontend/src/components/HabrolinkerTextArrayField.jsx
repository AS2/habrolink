import TypeTextCombinedFalseFil from "./TypeTextCombinedFalseFil";
import styles from "./HabrolinkerTextField.module.css";
import {useCallback, useState} from "react";

const HabrolinkerTextArrayField = ({ label, placeholder, value, onChangeValue }) => {
    const [currentTextArray, setCurrentTextArray] = useState(value == null ? "" : value.join());
    const [helperText, setHelperText] = useState(value == null ? "0/100" : String(value.length) + "/100");

    const onValueChanged = useCallback(event => {
        let curValue = event.target.value;
        setCurrentTextArray(curValue)
        curValue = curValue.split(",")
        curValue = curValue.map(s => s.trim());

        if (curValue[curValue.length - 1] == "")
            curValue.pop()

        setHelperText(String(curValue.length) + "/100")
        if (onChangeValue != null)
            onChangeValue(curValue);
    }, [helperText, currentTextArray]);

  return (
      <div className={styles.textField}>
          <div className={styles.partInputLabel}>
              <b className={styles.label}>{label}</b>
          </div>
          <input className={styles.inputField} onInput={onValueChanged} value={currentTextArray}
                 placeholder={placeholder}/>
          <div className={styles.partInputHelper}>
              <div className={styles.helperText}>Значения разделяются запятой. Считано {helperText} значений</div>
          </div>
      </div>
  );
};

export default HabrolinkerTextArrayField;
