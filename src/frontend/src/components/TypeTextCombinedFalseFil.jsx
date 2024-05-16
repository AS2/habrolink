import { useMemo } from "react";
import styles from "./TypeTextCombinedFalseFil.module.css";

const TypeTextCombinedFalseFil = ({
  placeholder,
  partFieldContentPlaceHeight,
  placeholderLineHeight,
  placeholderFontFamily,
  placeholderColor,
  placeholderFlex,
}) => {
  const partFieldContentPlaceStyle = useMemo(() => {
    return {
      height: partFieldContentPlaceHeight,
    };
  }, [partFieldContentPlaceHeight]);

  const placeholderStyle = useMemo(() => {
    return {
      lineHeight: placeholderLineHeight,
      fontFamily: placeholderFontFamily,
      color: placeholderColor,
      flex: placeholderFlex,
    };
  }, [
    placeholderLineHeight,
    placeholderFontFamily,
    placeholderColor,
    placeholderFlex,
  ]);

  return (
    <div className={styles.typetextCombinedfalseFil}>
      <div
        className={styles.partFieldContentPlace}
        style={partFieldContentPlaceStyle}
      >
        <div className={styles.placeholder} style={placeholderStyle}>
          {placeholder}
        </div>
      </div>
    </div>
  );
};

export default TypeTextCombinedFalseFil;
