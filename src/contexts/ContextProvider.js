import React, { createContext, useContext, useEffect, useState } from 'react'
import { cartData } from '../data/dummy'

const StateContext = createContext()
// Instead of using React.createContext, we just import the createContext directly from the react library

const initialState = {
  chat: false,
  cart: false,
  userProfile: false,
  notification: false,
}

export const ContextProvider = ({ children }) => {
  const [activeMenu, setActiveMenu] = useState(true)
  const [isClicked, setIsClicked] = useState(initialState)
  const [screenSize, setScreenSize] = useState(undefined)
  const [currentColor, setCurrengColor] = useState('#03C9D7')
  const [currentMode, setCurrentMode] = useState('Light')
  const [themeSettings, setThemeSettings] = useState(false)
  const [cart, setCart] = useState(cartData)
  const [total, setTotal] = useState(
    0
    // cart.map((item) => {
    //   let totalPrice = parseInt(item.amount) * parseInt(item.price)
    //   totalPrice += totalPrice
    //   return totalPrice
    // })
  )

  const increaseAmount = (cartId) => {
    
  }

  const decreaseAmount = (cartId) => {
    
  }

  // const totalAmount = () => {
  //   let { total, amount } = cart.reduce((cartTotal, cartItem) => {
  //     const { price, amount } = cartItem
  //     const itemTotal = price * amount
  //     cartTotal.total += itemTotal
  //     // cartTotal.amount += amount

  //     return cartTotal
  //   }, (total = 0))
  // }
  const setMode = (e) => {
    setCurrentMode(e.target.value)
    localStorage.setItem('themeMode', e.target.value)
    setThemeSettings(false)
  }

  const setColor = (newcolor) => {
    setCurrengColor(newcolor)
    localStorage.setItem('themeColor', newcolor)
    setThemeSettings(false)
  }
  const handleClick = (clicked) => {
    setIsClicked({ ...initialState, [clicked]: true })
  }

  // useEffect(() => {
  //   increaseAmount()
  // }, [])

  return (
    <StateContext.Provider
      value={{
        activeMenu,
        setActiveMenu,
        isClicked,
        setIsClicked,
        handleClick,
        screenSize,
        setScreenSize,
        currentColor,
        currentMode,
        setCurrengColor,
        setThemeSettings,
        themeSettings,
        setColor,
        setMode,
        increaseAmount,
        decreaseAmount,
        cart,
        total,
      }}
    >
      {children}
    </StateContext.Provider>
  )
}

export const useStateContext = () => useContext(StateContext)
