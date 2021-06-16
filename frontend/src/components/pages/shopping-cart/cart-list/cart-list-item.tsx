import React, { useState } from 'react'
import { CounterInput } from '../../../shared/counter-input'
import { CartProductInfo } from '../../../../types/cart'
import { cartStore } from '../../../../store/cart-store'
import { useProduct } from '../../../../hooks/useProduct'
import { Loader } from '../../../shared/loader/loader'

type Props = {
  item: CartProductInfo
}

export const CartListItem = ({ item }: Props) => {
  const { product, isLoading } = useProduct(item.product)

  const [buyQuantity, setBuyQuantity] = useState(item.quantity)

  if (isLoading)
    return <tr>
      <td style={{ width: '100%' }}><Loader/></td>
    </tr>

  return (
    <tr>
      <td>
        <figure className="itemside align-items-center">
          <div className="aside">
            <img
              alt="" src={product?.photo || ''}
              className="img-sm"
              style={{ objectFit: 'contain' }}/>
          </div>
          <figcaption className="info">
            <a href="#" className="title text-dark">{product?.title}</a>
            <p className="text-muted small">Brand: {product?.brand.title}</p>
          </figcaption>
        </figure>
      </td>
      <td>
        <CounterInput
          onBlur={async () => {
            await cartStore.updateProduct(item.product, buyQuantity)
            cartStore.loadCart()
          }}
          value={buyQuantity} setValue={setBuyQuantity}
          min={1} max={item.quantity}/>
      </td>
      <td>
        <div className="price-wrap">
          <var className="price">${(Number(product?.price) || 0) * buyQuantity}</var>
          <small className="text-muted">${product?.price} each</small>
        </div>
      </td>
      <td className="text-right d-none d-md-block">
        <a data-original-title="Save to Wishlist" title="" href="" className="btn btn-light" data-toggle="tooltip">
          Review
        </a>
        <button onClick={() => cartStore.removeProduct(item.product)} className="btn btn-light">Remove</button>
      </td>
    </tr>
  )
}
