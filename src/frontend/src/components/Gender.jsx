import { useMemo } from "react";
import PartFieldStyle from "./PartFieldStyle";
import EmptyTrueHelpFalseError from "./EmptyTrueHelpFalseError";
import styles from "./Gender.module.css";

const Gender = ({
  label,
  placeholder,
  standardChevronDown,
  propHeight,
  propWidth,
  propAlignSelf,
}) => {
  const genderStyle = useMemo(() => {
    return {
      height: propHeight,
    };
  }, [propHeight]);

  const partInputLabelStyle = useMemo(() => {
    return {
      width: propWidth,
      alignSelf: propAlignSelf,
    };
  }, [propWidth, propAlignSelf]);

  return (
    <div className={styles.gender} style={genderStyle}>
      <div className={styles.partInputLabel} style={partInputLabelStyle}>
        <b className={styles.label}>{label}</b>
      </div>
      <PartFieldStyle
        placeholder="Мужчина"
        standardChevronDown="/standard--chevrondown.svg"
      />
      <EmptyTrueHelpFalseError />
    </div>
  );
};

export default Gender;
