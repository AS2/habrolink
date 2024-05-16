import TypeTextCombinedFalseFil from "./TypeTextCombinedFalseFil";
import styles from "./Skills.module.css";

const Skills = ({ label, placeholder, helperText }) => {
  return (
    <div className={styles.skills}>
      <div className={styles.partInputLabel}>
        <b className={styles.label}>{label}</b>
      </div>
      <TypeTextCombinedFalseFil
        placeholder="Скачки, Гадание, Софтскился"
        partFieldContentPlaceHeight="24px"
        placeholderLineHeight="20px"
        placeholderFontFamily="'Noto Sans'"
        placeholderColor="#23272e"
        placeholderFlex="1"
      />
      <div className={styles.partInputHelper}>
        <b className={styles.helperText}>{helperText}</b>
      </div>
    </div>
  );
};

export default Skills;
