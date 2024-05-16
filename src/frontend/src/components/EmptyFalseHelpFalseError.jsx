import styles from "./EmptyFalseHelpFalseError.module.css";

const EmptyFalseHelpFalseError = ({ helperText }) => {
  return (
    <div className={styles.emptyfalseHelpfalseError}>
      <img className={styles.statusWarning} alt="" src="/status--warning.svg" />
      <b className={styles.helperText}>{helperText}</b>
    </div>
  );
};

export default EmptyFalseHelpFalseError;
