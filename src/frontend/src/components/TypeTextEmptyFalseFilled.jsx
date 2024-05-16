import { useMemo } from "react";
import styles from "./TypeTextEmptyFalseFilled.module.css";

const TypeTextEmptyFalseFilled = ({
  placeholderText,
  typeTextEmptyFalseFilledPadding,
  typeTextEmptyFalseFilledBorderRadius,
  typeTextEmptyFalseFilledBackgroundColor,
  typeTextEmptyFalseFilledAlignSelf,
  typeTextEmptyFalseFilledHeight,
  placeholderLineHeight,
  placeholderFontFamily,
  placeholderColor,
  placeholderFlex,
}) => {
  const typeTextEmptyFalseFilledStyle = useMemo(() => {
    return {
      padding: typeTextEmptyFalseFilledPadding,
      borderRadius: typeTextEmptyFalseFilledBorderRadius,
      backgroundColor: typeTextEmptyFalseFilledBackgroundColor,
      alignSelf: typeTextEmptyFalseFilledAlignSelf,
      height: typeTextEmptyFalseFilledHeight,
    };
  }, [
    typeTextEmptyFalseFilledPadding,
    typeTextEmptyFalseFilledBorderRadius,
    typeTextEmptyFalseFilledBackgroundColor,
    typeTextEmptyFalseFilledAlignSelf,
    typeTextEmptyFalseFilledHeight,
  ]);

  const placeholder1Style = useMemo(() => {
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
    <div
      className={styles.typetextEmptyfalseFilled}
      style={typeTextEmptyFalseFilledStyle}
    >
      <div className={styles.placeholder} style={placeholder1Style}>
        {placeholderText}
      </div>
    </div>
  );
};

export default TypeTextEmptyFalseFilled;
