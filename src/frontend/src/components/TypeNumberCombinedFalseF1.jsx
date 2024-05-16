import styles from "./TypeNumberCombinedFalseF1.module.css";

const TypeNumberCombinedFalseF1 = ({ placeholder }) => {
  return (
    <div className={styles.typenumberCombinedfalseF}>
      <div className={styles.partFieldContentPlace}>
        <div className={styles.placeholder}>{placeholder}</div>
      </div>
      <div className={styles.partFieldStyleNumber}>
        <img
          className={styles.standardChevronUp}
          alt=""
          src="/standard--chevronup.svg"
        />
        <img
          className={styles.standardChevronUp}
          alt=""
          src="/standard--chevrondown1.svg"
        />
      </div>
    </div>
  );
};

export default TypeNumberCombinedFalseF1;
