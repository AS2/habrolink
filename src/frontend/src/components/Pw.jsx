import TypeTextCombinedFalseFil from "./TypeTextCombinedFalseFil";
import EmptyTrueHelpFalseError from "./EmptyTrueHelpFalseError";
import styles from "./Pw.module.css";

const Pw = () => {
  return (
    <div className={styles.pw}>
      <div className={styles.partInputLabel}>
        <b className={styles.label}>Пароль</b>
      </div>
      <TypeTextCombinedFalseFil
        placeholder="****************"
        partFieldContentPlaceHeight="unset"
        placeholderLineHeight="24px"
        placeholderFontFamily="Roboto"
        placeholderColor="#494949"
        placeholderFlex="unset"
      />
      <EmptyTrueHelpFalseError />
    </div>
  );
};

export default Pw;
