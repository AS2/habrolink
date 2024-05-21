import styles from "./HabrolinkerPasswordFields.module.css";
import { useCallback, useState } from "react";
import EmptyFalseHelpFalseError from "./EmptyFalseHelpFalseError";

const HabrolinkerPasswordFields = ({ label1, label2, onChangeValue }) => {
    const [current1Password, setCurrent1PasswordText] = useState("");
    const [current2Password, setCurrent2PasswordText] = useState("");

    const onValue1Changed = useCallback(event => {
        let curValue = event.target.value;
        setCurrent1PasswordText(curValue)
        if (onChangeValue != null)
            onChangeValue(curValue == current2Password ? curValue : null);
    }, [current1Password, current2Password]);

    const onValue2Changed = useCallback(event => {
        let curValue = event.target.value;
        setCurrent2PasswordText(curValue)
        if (onChangeValue != null)
            onChangeValue(current1Password == curValue ? current1Password : null);
    }, [current1Password, current2Password]);

    return (
        <div className={styles.textField}>
            <div className={styles.partInputLabel}>
                <b className={styles.label}>{label1}</b>
            </div>
            <input type="password" className={styles.inputField} onInput={onValue1Changed} value={current1Password} />
            <div className={styles.partInputLabel}>
                <b className={styles.label}>{label2}</b>
            </div>
            <input type="password" className={styles.inputField} onInput={onValue2Changed} value={current2Password} />
            {(current1Password != current2Password) &&
                <div className={styles.errorHelper}>
                    <img className={styles.errorHelperWarning} alt="" src="/status--warning.svg" />
                    <b className={styles.errorHelperText}>Пароли не совпадают</b>
                </div>
            }
        </div>
    );
};

export default HabrolinkerPasswordFields;
