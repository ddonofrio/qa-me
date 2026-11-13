export function invoice(amount, email) {
  return { id: Date.now(), amount, email };
}
