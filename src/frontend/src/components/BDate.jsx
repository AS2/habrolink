import PartFieldStyle1 from "./PartFieldStyle1";
import EmptyTrueHelpFalseError from "./EmptyTrueHelpFalseError";
import styles from "./BDate.module.css";

const BDate = () => {
  return (
    <div className={styles.bdate}>
      <div className={styles.partInputLabel}>
        <b className={styles.label}>Дата рождения</b>
      </div>
      <PartFieldStyle1 />
      <EmptyTrueHelpFalseError />
    </div>
  );
};

export default BDate;
