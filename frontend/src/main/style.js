import styled from 'styled-components';

export const MainWapper = styled.div`
background: #ECF5FF;
min-width: 100vh;
min-height: 98vh;
`
export const CategoryWapper = styled.div`
background: #C4E1FF;
min-width: 1040px;
height: 70px;
border-bottom: 3px solid black;
`

export const Categoryoption = styled.div`
position: relative;
border-right: 1px solid black;
margin: auto;
text-align: center;
font-size: 20px;
height: 70px;
width: 100px;
padding: 0 15px;
float: left;
line-height: 70px;
cursor: pointer;
&.mousein {
  background: #97CBFF;
}
`

export const ComponentWapper = styled.div`
background: #ECF5FF;
`

export const ComponentoptionWapper = styled.div`
margin: 20px 0 0 25px;
overflow: hidden;
`;

export const Componentindex = styled.div`
text-align: center;
margin-left: 30px;
line-height: 30px;
height: 30px;
width: 120px;
border-radius: 7px;
font-size: 18px;
background: #BEBEBE;
float: left;
`;

export const Componentinput = styled.input`
rows: 1;
resize: none;
padding: 0 5px;
line-height: 30px;
height: 30px;
width: 200px;
border-radius: 7px;
font-size: 18px;
border: none;
outline: none;
margin-left: 30px;
background: #e0e0e0;
&.bigbox {
width: 500px;
height: 250px;
}
`;

export const Componentbutton = styled.div`
text-align: center;
margin: 20px 0 0 55px;
line-height: 30px;
height: 30px;
width: 100px;
border-radius: 7px;
font-size: 18px;
cursor: pointer;
float: left;
background: #97CBFF;
&.reject {
color: red;
}
`;