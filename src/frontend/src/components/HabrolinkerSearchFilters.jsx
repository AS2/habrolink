import { useCallback } from "react";
import StyleOutlineTypetextClea from "./StyleOutlineTypetextClea";
import styles from "./HabrolinkerSearchFilters.module.css";

import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import HabrolinkerTextField from "./HabrolinkerTextField";
import HabrolinkerTextArrayField from "./HabrolinkerTextArrayField";

const HabrolinkerSearchFilters = ({ onSubmitClick, filters, filtersSetter}) => {

  function onSource(event) {
    event.persist();

    filtersSetter((oldFilters) => ({
      ...oldFilters,
      source: event.target.value
    }))
  }

  function onRatingLow(event) {
    event.persist();

    filtersSetter((oldFilters) => ({
      ...oldFilters,
      habr_rating_low: event.target.value
    }))
  }

  function onRatingHigh(event) {
    event.persist();

    filtersSetter((oldFilters) => ({
      ...oldFilters,
      habr_rating_high: event.target.value
    }))
  }

  function onKarmaLow(event) {
    event.persist();

    filtersSetter((oldFilters) => ({
      ...oldFilters,
      habr_karma_low: event.target.value
    }))
  }
  function onKarmaHigh(event) {
    event.persist();

    filtersSetter((oldFilters) => ({
      ...oldFilters,
      habr_karma_high: event.target.value
    }))
  }

  function onAgeLow(event) {
    event.persist();

    filtersSetter((oldFilters) => ({
      ...oldFilters,
      age_low: event.target.value
    }))
  }
  function onAgeHigh(event) {
    event.persist();

    filtersSetter((oldFilters) => ({
      ...oldFilters,
      age_high: event.target.value
    }))
  }

  function onSalaryLow(event) {
    event.persist();

    filtersSetter((oldFilters) => ({
      ...oldFilters,
      salary_low: event.target.value
    }))
  }
  function onSalaryHigh(event) {
    event.persist();

    filtersSetter((oldFilters) => ({
      ...oldFilters,
      salary_high: event.target.value
    }))
  }

  function onLocCountry(data) {
    filtersSetter((oldFilters) => ({
      ...oldFilters,
      location_country: data
    }))
  }

  function onLocRegion(data) {
    filtersSetter((oldFilters) => ({
      ...oldFilters,
      location_region: data
    }))
  }

  function onLocCity(data) {
    filtersSetter((oldFilters) => ({
      ...oldFilters,
      location_city: data
    }))
  }

  function onSpeciality(data) {
    filtersSetter((oldFilters) => ({
      ...oldFilters,
      speciality: data
    }))
  }

  function onSkill(data) {
    filtersSetter((oldFilters) => ({
      ...oldFilters,
      skills: data
    }))
  }

  return (
    <div className={styles.filtersBlock}>

      <div className={styles.userPlatform}>
        <b className={styles.b}>Откуда пользователь?</b>

        <Form>
          <Form.Check value={0} onChange={onSource} label="С любой платформы" name="sourceGroup" type='radio' id={`inline-radio-3`} checked={filters.source == 0} />
          <Form.Check value={1} onChange={onSource} label="С ХаброЛинкера" name="sourceGroup" type='radio' id={`inline-radio-1`} checked={filters.source == 1}/>
          <Form.Check value={2} onChange={onSource} label="С Хабра" name="sourceGroup" type='radio' id={`inline-radio-2`} checked={filters.source == 2}/>
        </Form>
      </div>

      <b className={styles.b}>Рейтинг Хабра</b>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="minRating">
          <Form.Label column sm="2">
            Min:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" value={filters.habr_rating_low} onChange={onRatingLow}/>
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="maxRating">
          <Form.Label column sm="2">
            Max:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" value={filters.habr_rating_high} onChange={onRatingHigh}/>
          </Col>
        </Form.Group>
      </Form>

      <b className={styles.b}>Карма Хабра</b>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="minCarma">
          <Form.Label column sm="2">
            Min:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" value={filters.habr_karma_low} onChange={onKarmaLow}/>
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="maxCarma">
          <Form.Label column sm="2">
            Max:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" value={filters.habr_karma_high} onChange={onKarmaHigh}/>
          </Col>
        </Form.Group>
      </Form>

      <b className={styles.b}>Возраст</b>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="minAge">
          <Form.Label column sm="2">
            Min:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" value={filters.age_low} onChange={onAgeLow}/>
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="maxAge">
          <Form.Label column sm="2">
            Max:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" value={filters.age_high} onChange={onAgeHigh}/>
          </Col>
        </Form.Group>
      </Form>

      <div className={styles.place}>
        <b className={styles.b}>Место</b>
        <div className={styles.placeFields}>
          <HabrolinkerTextField key={"country"} label="" placeholder="Страна" value={filters.location_country} onChangeValue={onLocCountry}/>
          <HabrolinkerTextField key={"region"} label="" placeholder="Район" value={filters.location_region} onChangeValue={onLocRegion}/>
          <HabrolinkerTextField key={"city"} label="" placeholder="Город" value={filters.location_city} onChangeValue={onLocCity}/>
        </div>
      </div>

      <b className={styles.b}>Зарплата (в долларах)</b>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="minSalary">
          <Form.Label column sm="2">
            Min:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" value={filters.salary_low} onChange={onSalaryLow}/>
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="maxSalary">
          <Form.Label column sm="2">
            Max:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" value={filters.salary_high} onChange={onSalaryHigh}/>
          </Col>
        </Form.Group>
      </Form>

      <div className={styles.place}>
        <b className={styles.b}>Специальности</b>
        <HabrolinkerTextArrayField key={"speciality"} label=""
                                   placeholder={["Fullstack Developer", "Game Developer"]}
                                   value={filters.speciality}
                                   onChangeValue={onSpeciality}/>
      </div>
      <div className={styles.place}>
        <b className={styles.b}>Навыки</b>
        <div className={styles.specialitiesField1}>
          <HabrolinkerTextArrayField key={"skill"} label="" placeholder={["С++", "Python", "Git"]}
                                     value={filters.skill}
                                     onChangeValue={onSkill}/>
        </div>
      </div>

      <Form>
        <Form.Group className="mb-3" controlId="submit">
          <Form.Control type="button" defaultValue="Поиск" onClick={onSubmitClick} />
        </Form.Group>
      </Form>
    </div>
  );
};

export default HabrolinkerSearchFilters;
