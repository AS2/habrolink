import styles from "./PartFieldStyle.module.css";

const PartFieldStyle = ({ placeholder, standardChevronDown }) => {
  return (
    <div className={styles.partFieldStyle}>
      <div className={styles.partFieldContentPlace}>
        <div className={styles.placeholder}>{placeholder}</div>
      </div>
      <img
        className={styles.standardSelectDictionary}
        alt=""
        src={standardChevronDown}
      />
    </div>
  );
};

export default PartFieldStyle;
