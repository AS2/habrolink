import TypeNumberCombinedFalseF1 from "./TypeNumberCombinedFalseF1";
import EmptyTrueHelpFalseError from "./EmptyTrueHelpFalseError";
import styles from "./Salary.module.css";

const Salary = () => {
  return (
    <div className={styles.salary}>
      <div className={styles.partInputLabel}>
        <b className={styles.label}>Доход (в фунтах)</b>
      </div>
      <TypeNumberCombinedFalseF1 placeholder="152" />
      <EmptyTrueHelpFalseError />
    </div>
  );
};

export default Salary;
