function Card(props) {
  return (
    <div className="card">
      <h2>{props.name}</h2>
      <p>Age: {props.age}</p>
      <p>Department: {props.department}</p>
      <p>College: {props.college}</p>
    </div>
  );
}

export default Card;