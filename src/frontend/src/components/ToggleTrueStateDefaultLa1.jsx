import { useMemo } from "react";
import styles from "./ToggleTrueStateDefaultLa1.module.css";

const ToggleTrueStateDefaultLa1 = ({
  checkBoxVariant14,
  label,
  labelTextTransform,
}) => {
  const label1Style = useMemo(() => {
    return {
      textTransform: labelTextTransform,
    };
  }, [labelTextTransform]);

  return (
    <div className={styles.toggletrueStatedefaultLa}>
      <img
        className={styles.checkboxvariant14Icon}
        alt=""
        src={checkBoxVariant14}
      />
      <div className={styles.label} style={label1Style}>
        {label}
      </div>
    </div>
  );
};

export default ToggleTrueStateDefaultLa1;
