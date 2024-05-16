import { useMemo } from "react";
import styles from "./StyleOutlineTypetextClea.module.css";

const StyleOutlineTypetextClea = ({
  label = "Label ",
  styleOutlineTypetextCleaBorder,
}) => {
  const styleOutlineTypetextCleaStyle = useMemo(() => {
    return {
      border: styleOutlineTypetextCleaBorder,
    };
  }, [styleOutlineTypetextCleaBorder]);

  return (
    <div
      className={styles.styleoutlineTypetextClea}
      style={styleOutlineTypetextCleaStyle}
    >
      <div className={styles.label}>{label}</div>
      <img className={styles.clearIcon} alt="" src="/clear.svg" />
    </div>
  );
};

export default StyleOutlineTypetextClea;
