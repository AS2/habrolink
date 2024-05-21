import styles from "./HabrolinkerPageChooser.module.css";

const HabrolinkerPageChooser = ({current, amount, onChangeValue}) => {
    function onClick(pageNum) {
        onChangeValue(pageNum);
    }

    let buttons = []
    if (amount > 1) {
        buttons.push({string: "<<", value: Math.max(current - 1, 0)})
        if (current != 0 && current != 1)
            buttons.push({string: "1", value: 0})
        if (current - 1 > 1)
            buttons.push({string: "...", value: 0})

        if (current != 0)
            buttons.push({string: (current).toString(), value: current - 1})
        buttons.push({string: (current + 1).toString(), value: current})
        if (current + 1 < amount)
            buttons.push({string: (current + 2).toString(), value: current + 1})

        if (current + 1 < amount - 2) {
            buttons.push({string: "...", value: 0})
        }

        if (current != amount - 1 && current != amount - 2) {
            buttons.push({string: (amount).toString(), value: amount - 1})
        }
        buttons.push({string: ">>", value: Math.min(current + 1, amount - 1)})
    }
    let reactButtons = []
    for (let i = 0; i < buttons.length; i++) {
        if (buttons[i].string == "...")
        {
            reactButtons.push(<div key={i} className={styles.button}>{buttons[i].string}</div>);
        }
        else if (buttons[i].string == "<<" || buttons[i].string == ">>")
        {
            reactButtons.push(<div key={i} className={styles.button} onClick={() => onClick(buttons[i].value)}>{buttons[i].string}</div>);
        }
        else if (current == buttons[i].value)
        {
            reactButtons.push(<div key={i} className={styles.choosedButton}>{buttons[i].string}</div>);
        }
        else
        {
            reactButtons.push(<div key={i} className={styles.button} onClick={() => onClick(buttons[i].value)}>{buttons[i].string}</div>);
        }
    }
    return (
        <div className={styles.pages}>
            {
                reactButtons
            }

        </div>
    );
};

export default HabrolinkerPageChooser;
