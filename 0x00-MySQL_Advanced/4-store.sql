-- reate a trigger to update quantity after inserting a new order
DELIMITER //
CREATE TRIGGER update_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity in the items table based on the new order
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER;
