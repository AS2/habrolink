import { useMemo } from "react";
import styles from "./PartFieldStyleNumber.module.css";

const PartFieldStyleNumber = ({ partFieldStyleNumberGap }) => {
  const partFieldStyleNumberStyle = useMemo(() => {
    return {
      gap: partFieldStyleNumberGap,
    };
  }, [partFieldStyleNumberGap]);

  return (
    <div
      className={styles.partFieldStyleNumber}
      style={partFieldStyleNumberStyle}
    >
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
  );
};

export default PartFieldStyleNumber;
