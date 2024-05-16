import TypeTextCombinedFalseFil from "./TypeTextCombinedFalseFil";
import styles from "./City.module.css";

const City = ({ label, placeholder, helperText }) => {
  return (
    <div className={styles.city}>
      <div className={styles.partInputLabel}>
        <b className={styles.label}>{label}</b>
      </div>
      <TypeTextCombinedFalseFil
        placeholder="Смоллхит"
        partFieldContentPlaceHeight="unset"
        placeholderLineHeight="24px"
        placeholderFontFamily="Roboto"
        placeholderColor="#494949"
        placeholderFlex="unset"
      />
      <div className={styles.partInputHelper}>
        <div className={styles.helperText}>{helperText}</div>
      </div>
    </div>
  );
};

export default City;
