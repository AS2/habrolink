import TypeTextCombinedFalseFil from "./TypeTextCombinedFalseFil";
import EmptyFalseHelpFalseError from "./EmptyFalseHelpFalseError";
import styles from "./PwAgain.module.css";

const PwAgain = () => {
  return (
    <div className={styles.pwAgain}>
      <div className={styles.partInputLabel}>
        <b className={styles.label}>Повторите пароль</b>
      </div>
      <TypeTextCombinedFalseFil
        placeholder="****************"
        partFieldContentPlaceHeight="unset"
        placeholderLineHeight="24px"
        placeholderFontFamily="Roboto"
        placeholderColor="#494949"
        placeholderFlex="unset"
      />
      <EmptyFalseHelpFalseError helperText="Пароли не совпадают" />
    </div>
  );
};

export default PwAgain;
