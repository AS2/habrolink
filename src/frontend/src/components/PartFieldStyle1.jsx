import TypeTextEmptyFalseFilled from "./TypeTextEmptyFalseFilled";
import styles from "./PartFieldStyle1.module.css";

const PartFieldStyle1 = () => {
  return (
    <div className={styles.partFieldStyle}>
      <img
        className={styles.standardCalendar}
        alt=""
        src="/standard--calendar.svg"
      />
      <TypeTextEmptyFalseFilled
        placeholderText="18.04.1884"
        typeTextEmptyFalseFilledPadding="var(--padding-11xs) 0px"
        typeTextEmptyFalseFilledBorderRadius="unset"
        typeTextEmptyFalseFilledBackgroundColor="unset"
        typeTextEmptyFalseFilledAlignSelf="unset"
        typeTextEmptyFalseFilledHeight="unset"
        placeholderLineHeight="20px"
        placeholderFontFamily="'Noto Sans'"
        placeholderColor="#23272e"
        placeholderFlex="unset"
      />
      <img
        className={styles.standardCalendar}
        alt=""
        src="/standard--close.svg"
      />
    </div>
  );
};

export default PartFieldStyle1;
