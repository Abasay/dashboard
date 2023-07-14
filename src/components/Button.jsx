import React from 'react'
import { useStateContext } from '../contexts/ContextProvider'

const Button = ({
  bgColor,
  color,
  size,
  text,
  borderRadius,
  icon,
  category,
}) => {
  const { isClicked, setIsClicked } = useStateContext()
  return (
    <button
      type='button'
      style={{ backgroundColor: bgColor, color, borderRadius }}
      className={`text_${size} p-3 hover:drop-shadow-xl`}
      onClick={() => setIsClicked(!isClicked.category)}
    >
      {text ? text : icon}
    </button>
  )
}

export default Button
