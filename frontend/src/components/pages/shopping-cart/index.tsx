import React from 'react'
import { PaymentForm } from './payment-form'
import { CartList } from './cart-list/cart-list'

export const ShoppingCart = () => {

  return (
    <div className="container" style={{ padding: 25 }}>
      <div className="row">
        <aside className="col-lg-9">
          <div className="card">
            <div className="table-responsive">
              <table className="table table-borderless table-shopping-cart">
                {/*eslint-disable*/}
                <thead className="text-muted">
                <tr className="small text-uppercase">
                  <th scope="col">Product</th>
                  <th scope="col" style={{ width: 120 }}>Quantity</th>
                  <th scope="col" style={{ width: 120 }}>Price</th>
                  <th scope="col" className="text-right d-none d-md-block" style={{ width: 200 }}/>
                </tr>
                </thead>
                <tbody>
                <CartList/>
                </tbody>
                {/* eslint-enable */}
              </table>
            </div>
          </div>
        </aside>
        <PaymentForm/>
      </div>
    </div>
  )
}
